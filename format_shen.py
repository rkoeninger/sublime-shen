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

class Cons(Expression):
	def __init__(self, raw, elements, tail):
		Base.__init__(self, raw)
		self.elements = elements
		self.tail = tail

class Application(Expression):
	def __init__(self, raw, elements):
		Base.__init__(self, raw)
		self.elements = elements

# also need special forms for:
#   if, cases, cond, defmacro, defprolog, defcc, datatype, package

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

	def format(self, content):
		return content

	def parse(content, index):
		if content[index] == ' ':
			# skip whitespace
			return parse(content, index + 1)
		elif content[index] == '(':
			# parse children
		elif content[index] == '[':
			# parse children
		elif content[index] == '"':
			# parse string
		else:
			# parse number, symbol
		return 0
