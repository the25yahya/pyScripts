#a script that allows users to view and manage running processes on their system. Users can list all processes, kill specific processes by name or PID, and view detailed information about individual processes.
import psutil

def list_processes():
    proc = psutil.pids()
    results = []
    for pid in proc:
        try:
            p = psutil.Process(pid)
            name = p.name()
            results.append((pid, name))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    for result in results:
        print(result)

def manage_process(action):
    process_input = input("Enter Process Name or ID: ").lower()
    try:
        process_id = int(process_input)
    except ValueError:
        process_id = None

    process_found = False

    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            if process_id is not None and p.pid == process_id:
                perform_action(p, action)
                process_found = True
                break
            elif p.name().lower() == process_input:
                perform_action(p, action)
                process_found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not process_found:
        print(f"==No process found with {'ID' if process_id else 'name'}: {process_input}==")

def perform_action(process, action):
    actions = {
        'kill': process.kill,
        'terminate': process.terminate,
        'suspend': process.suspend,
        'resume': process.resume,
        'info': lambda: print(f"""
            -\033[91m\033[1mPROCESS ID\033[0m: {process.pid}
            -\033[91m\033[1mPROCESS NAME\033[0m: {process.name()}
            -\033[91m\033[1mPROCESS STATUS\033[0m: {process.status()}
            -\033[91m\033[1mPROCESS EXECUTABLE\033[0m: {process.exe()}
            -\033[91m\033[1mPROCESS CMDLINE\033[0m: {process.cmdline()}
            -\033[91m\033[1mPROCESS PARENT\033[0m: {process.parent()}
            -\033[91m\033[1mMEMORY INFORMATION\033[0m: {process.memory_info()}
            -\033[91m\033[1mOPEN FILES\033[0m: {process.open_files()}
            -\033[91m\033[1mNUMBER OF THREADS\033[0m: {process.num_threads()}
            -\033[91m\033[1mPROCESS THREADS\033[0m: {process.threads()}
        """)
    }
    try:
        actions[action]()
        if action != 'info':
            print(f"Process {process.pid} {action}ed successfully.")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        print(f"Failed to {action} process: {e}")

CHOICE = input("""==== ENTER AN OPTION FROM THE FOLLOWING (use option number):
               1-List all running processes
               2-Kill a specific process by name or ID
               3-Suspend a specific process by name or ID
               4-Terminate a specific process by name or ID
               5-Resume a suspended process by name or ID
               6-View details about a specific process
               -""")

if CHOICE == "1":
    list_processes()
elif CHOICE == "2":
    manage_process('kill')
elif CHOICE == "3":
    manage_process('suspend')
elif CHOICE == "4":
    manage_process('terminate')
elif CHOICE == "5":
    manage_process('resume')
elif CHOICE == "6":
    manage_process('info')
else:
    print("Invalid option. Please enter a number between 1 and 6.")

