<#
Reference:
https://social.technet.microsoft.com/Forums/en-US/2263c5a7-41d4-4c64-96ee-46437aba1a85/
#>
$script = Resolve-Path("..\log.bat")

$scheduler = new-object -com("Schedule.Service")
$scheduler.Connect()

$folder = $scheduler.GetFolder("\")

$definition = $scheduler.NewTask(0)
$triggers = $definition.Triggers
$trigger = $triggers.Create(11) # TASK_TRIGGER_SESSION_STATE_CHANGE
$trigger.StateChange = 7 # TASK_SESSION_LOCK 
$action = $definition.Actions.Create(0)
$action.Path = [string]$script
$action.Arguments = "lock"
$folder.RegisterTaskDefinition("Lock Logging", $definition, 6, "", "" , 0)

$definition = $scheduler.NewTask(0)
$triggers = $definition.Triggers
$trigger = $triggers.Create(11) # TASK_TRIGGER_SESSION_STATE_CHANGE
$trigger.StateChange = 8 # TASK_SESSION_UNLOCK 
$action = $definition.Actions.Create(0)
$action.Path = [string]$script
$action.Arguments = "unlock"
$folder.RegisterTaskDefinition("Unlock Logging", $definition, 6, "", "" , 0)
