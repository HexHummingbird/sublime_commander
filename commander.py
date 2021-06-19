import sublime
import sublime_plugin
from Context import context as lib_context

class CommanderCommand(sublime_plugin.WindowCommand):
	def run(self, command_chain):
		command_tree(this.window, commands)
		
	def command_tree(self, window, command_chain):
		for item in command_chain:
			if "condition" in item:
				# then it is a pure condition
				context, context_true, context_false = item
				if lib_context.check(self.view, [context]):
					tree_to_run = context_true
				else:
					tree_to_run = context_false
				command_tree(window, tree_to_run)
			elif "name" in item:
				# then current item is a command
				name, args, context = item
				can_execute = True
				if context != None and not lib_context.check(self.view, [context]):
					can_execute = false
				if can_execute:
					window.run_command(name, args)
			elif isinstance(item, string):
				# then this is command shorthand
				window.run_command(item)



# class ChainCommand(sublime_plugin.WindowCommand):
#     def run(self, commands):
#         window = self.window
#         for command in commands:
#             command_name = command[0]
#             command_args = command[1:]
#             window.run_command(command_name, *command_args)

# class TestCommand(sublime_plugin.TextCommand):
#   def run(self, edit):
#     is_python_file = {
#       "key": "file_name",
#       "operator": "regex_contains",
#       "operand": "py$",
#     }

#     is_file_in_tests = {
#       "key": "file_name",
#       "operator": "regex_contains",
#       "operand": "/tests/",
#     }

#     if context.check(self.view, [is_python_file, is_file_in_tests]):
#       print("This file is python file in tests directory!")


"""
# Example 1
"commander": {
	"command_chain": [
		{
			"condition": {
				"context": "...",
				"context_true": [...], # <-- this array is another command_chain
				"context_false": [...] # <-- this array is another command_chain
			},
		},
		{
			"name": "some_command",
			"args": {...}, # <-- args to some_command
			"context": {...} # <-- context of some_command
		},
		{
			"name": "command_without_context",
			"args": {...}
		},
		{
			"name": "command_without_args",
			"context": {...}
		},
		{
			"name": "command_without_context_and_args"
		},
		"command_without_context_and_args_shorthand",
		...
	]
}

# Example 2
"commander": {
	"command_chain": [
		{
			"name": "name1",
			"args": {...},
			"condition": {
				"context": "...",
				"context_true": [...], # <-- this array is command_chain
				"context_false": [...] # <-- this array is command_chain
			},
		},
		{
			"name": "some_command",
			"args": {...}, # <-- args to some_command
			"context": {...} # <-- context of some_command
		},
		{
			"name": "command_without_context",
			"args": {...} # <-- args to command_without_context
		},
		{
			"name": "command_without_context_and_args"
		},
	]
} 


"""
