import win32com.client
import os

def register_task(scheduler, state_change, name, command, arguments):
    folder = scheduler.GetFolder('\\')

    definition = scheduler.NewTask(0)

    TASK_TRIGGER_SESSION_STATE_CHANGE = 11
    trigger = definition.Triggers.Create(TASK_TRIGGER_SESSION_STATE_CHANGE)
    trigger.StateChange = state_change

    TASK_ACTION_EXEC = 0
    action = definition.Actions.Create(TASK_ACTION_EXEC)
    action.Path = command
    action.Arguments = arguments

    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    NO_USER = ''
    NO_PASSWORD = ''
    folder.RegisterTaskDefinition(name, definition,
            TASK_CREATE_OR_UPDATE, NO_USER, NO_PASSWORD, TASK_LOGON_NONE)

script = os.path.abspath('..\log.py')
scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()

TASK_SESSION_LOCK = 7
TASK_SESSION_UNLOCK = 8
register_task(scheduler, TASK_SESSION_LOCK, 'Lock Logging', 'C:\\Windows\\pyw.exe' , script + ' lock')
register_task(scheduler, TASK_SESSION_UNLOCK, 'Unlock Logging', 'C:\\Windows\\pyw.exe' , script + ' unlock')
