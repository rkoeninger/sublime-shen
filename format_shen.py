import sublime
import sublime_plugin
import sys
import os

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
