import sublime
import sublime_plugin
import sys
import os

class Syntax(object):
  def __init__(self, raw):
    self.raw = raw

class LineComment(Syntax):
  def __init__(self, raw, content):
    Base.__init__(self, raw)
    self.content = content

class BlockComment(Syntax):
  def __init__(self, raw, content):
    Base.__init__(self, raw)
    self.content = content

class Expression(Syntax):
  def __init__(self, raw):
    Base.__init__(self, raw)

class Define(Expression):
  def __init__(self, raw, name, arity, typesig, clauses):
    Base.__init__(self, raw)
    self.name = name
    self.arity = arity
    self.typesig = typesig
    self.clauses = clauses

class Clause(Expression):
  def __init__(self, raw, params, backtrack, body, guard):
    Base.__init__(self, raw)
    self.params = params
    self.backtrack = backtrack
    self.body = body
    self.guard = guard

class Parens(Expression):
  def __init__(self, raw, children):
    Base.__init__(self, raw)
    self.children = children

class Squares(Expression):
  def __init__(self, raw, children):
    Base.__init__(self, raw)
    self.children = children

class Application(Expression):
  def __init__(self, raw, elements):
    Base.__init__(self, raw)
    self.elements = elements

# also need special forms for:
#   if, cases, cond, defmacro, defprolog, defcc, datatype, package


class Source(object):
  def __init__(self, raw):
    self.raw = raw
    self.length = len(raw)
    self.position = 0
    
  def is_done(self):
    return self.position >= self.length
    
  def skip(self, n):
    self.position = self.position + n

  def any_is_prefix(self, prefixes):
    for prefix in prefixes:
      if self.is_prefix(prefix):
        return True
    return False

  def skip_until_any(self, prefixes):
    while not(self.is_done()) and not(self.any_is_prefix(prefixes)):
      self.skip(1)
    
  def skip_until(self, prefix):
    self.skip_until_any([prefix])

  def skip_whitespace(self):
    while not(self.is_done()) and self.raw[self.position].isspace():
      self.skip(1)

  def is_prefix(self, prefix):
    return self.raw.startswith(prefix, self.position)

  def read_line_comment(self):
    self.skip(2)
    start = self.position
    self.skip_until("\n")
    end = self.position
    self.skip(1)
    return self.raw[start : end].strip()

  def read_block_comment(self):
    self.skip(2)
    start = self.position
    self.skip_until("*\\")
    end = self.position
    self.skip(2)
    return self.raw[start : end].strip()

  def read_string(self):
    self.skip(1)
    start = self.position
    self.skip_until("\"")
    end = self.position
    self.skip(1)
    return self.raw[start : end]

  def read_paren_list(self):
    start = self.position
    self.skip(1)
    children = []
    while not(self.is_done()) and not(self.is_prefix(")")):
      children.append(self.next())
      self.skip_whitespace()
    self.skip(1)
    end = self.position
    return Parens(raw[start : end], children)

  def read_square_list(self):
    start = self.position
    self.skip(1)
    children = []
    while not(self.is_done()) and not(self.is_prefix("]")):
      children.append(self.next())
      self.skip_whitespace()
    self.skip(1)
    end = self.position
    return Cons(raw[start : end], children)

  def read_atom(self):
    start = self.position
    self.skip_until_any(["(", ")", "[", "]", "{", "}", "\"", "\\\\", "\\*", " ", "\r", "\n", "\t"])
    end = self.position
    # need to process atom: number or symbol?
    return self.raw[start : end]

  def next(self):
    self.skip_whitespace()
    
    if (self.is_done()):
      return None
    elif self.is_prefix("\\\\"):
      return self.read_line_comment()
    elif self.is_prefix("\\*"):
      return self.read_block_comment()
    elif self.is_prefix("\""):
      return self.read_string()
    elif self.is_prefix("("):
      return self.read_paren_list()
    elif self.is_prefix("["):
      return self.read_square_list()
    else:
      return self.read_atom()

class Formatter(object):
  def __init__(self, indent):
    self.indent = indent

  def format(syntax):
    pass

class ShenFormatCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print 'format_shen begin'

    # Confirm this is a Shen file
    suffix_setting = self.view.settings().get('syntax')
    file_suffix = suffix_setting.split('.')[0]
    if file_suffix[-4:].lower() != 'shen': return

    # Get target code
    region = sublime.Region(0, self.view.size())
    content = self.view.substr(region)

    # Get cursor position
    selection = self.view.sel()[0].b
    row, col = self.view.rowcol(selection)

    # Replace target code with formatted code
    self.view.replace(edit, region, format(content))

    # Reset cursor position
    selection = self.view.full_line(self.view.text_point(row - 1, 0)).b
    cursor_pos = sublime.Region(selection, selection)
    regions = self.view.sel()
    regions.clear()
    regions.add(cursor_pos)
    sublime.set_timeout_async(lambda: self.view.show_at_center(cursor_pos), 0)

    print 'format_shen end'
