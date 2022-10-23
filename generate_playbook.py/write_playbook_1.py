import csv
from collections import OrderedDict, namedtuple

import yaml
from ansible.executor.task_queue_manager import TaskQueueManager
# from ansible.vars import VariableManager
# from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play

csvfile = open('sample-play.csv', 'r')
datareader = csv.reader(csvfile, delimiter=",", quotechar='"')
result = list()
type_index = -1
child_fields_index = -1

play_src = dict(
            name="",
            hosts="localhost",
            gather_facts="no",
            tasks=[])


# set options for play
Options = namedtuple('Options', ['connection', 'module_path', 'forks',
                                 'become', 'become_method', 'become_user', 'check'])

#initialize needed objects
# variable_manager = VariableManager()
loader = DataLoader()
options = Options(connection='local', module_path='', forks=100, become=True,
                  become_method='sudo', become_user='root', check=False)
passwords = dict(vault_pass='secret')


for row_index, row in enumerate(datareader):
  if row_index == 0:
    # let's do this once here
    data_headings = list()
    for heading_index, heading in enumerate(row):
      fixed_heading = heading.lower().replace(" ", "_").replace("-", "")

      data_headings.append(fixed_heading)

      if fixed_heading == "type":
        type_index = heading_index
      elif fixed_heading == "childfields":
        child_fields_index = heading_index

  else:
    content = dict()
    action = dict()
    args = dict()
    is_array = False
    for cell_index, cell in enumerate(row):

     if cell_index == 0:
          play_src['name'] = row[0]
          content['name'] = row[1]

     action[row[2]] = row[3]
     if cell_index == 4:
          action['args']= dict(x.split("=") for x in row[4].split(";"))

     content['action'] = action

     if cell_index == 5:
          content['with_items']= (row[5].split(";"))

    content['register']= row[6]

    play_src['tasks'] = content


     #  if cell_index == child_fields_index and is_array:
     #    content[data_headings[cell_index]] = [{
     #        "source" : "fra:" + value.capitalize(),
     #        "destination" : value,
     #        "type" : "string",
     #        "childfields" : "null"
     #      } for value in cell.split(",")]
     #  else:
     #    content[data_headings[cell_index]] = cell
     #    is_array = (cell_index == type_index) and (cell == "array")
     # #    if 'args' in content:
     #      # print(content)
    result.append(content)


# print(result)
print(yaml.dump(play_src))
#create inventory and pass to var manager
# inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
# variable_manager.set_inventory(inventory)

#create play with tasks
# play_src = dict(
#             name="Install and run a Docker container",
#             hosts="localhost",
#             gather_facts="no",
#             tasks=[
#                 dict(name="Install Dependencies", action=dict(module="apt", args=dict(name="{{ item }}", update_cache="yes")),
#                      with_items=["python-dev", "python-setuptools"]),
#
#                 dict(name="Install pip", action=dict(module="easy_install", args=dict(name="pip"))),
#
#                 dict(name="Install docker-py", action=dict(module="pip", args=dict(name="docker-py", state="present"))),
#
#                 dict(name="Add docker apt-repo", action=dict(module="apt_repository",
#                      args=dict(repo="deb https://apt.dockerproject.org/repo ubuntu-trusty main", state="present"))),
#
#                 dict(name="Import the Docker repository key", action=dict(module="apt_key",
#                      args=dict(url="https://apt.dockerproject.org/gpg", state="present", id="2C52609D"))),
#
#                 dict(name="Install Docker package", action=dict(module="apt",
#                      args=dict(name="docker-engine", update_cache="yes"))),
#
#                dict(name="Create a data container", action=dict(module="docker_container",
#                                                          args=dict(name="test", image="busybox", volumes="/data"))),
#
#                dict(name="Run a command", action=dict(module="command", args="docker run busybox /bin/echo 'hello world'"),
#                     register="output"),
#
#                dict(name="Output", action=dict(module="debug", args=dict(var="output.stdout_lines"))),
#              ],
#             # handlers=[dict(name="restart docker",
#             #                action=dict(module="service", args=dict(name="docker", state="restarted")))]
#         )
# # print(play_src)
# playbook_file = yaml.dump(play_src)
# print(playbook_file)
#
with open(r'store_file_1.yml', 'w') as file:
    documents = yaml.safe_dump(play_src, file, sort_keys=False, default_flow_style=False)
#     documents = yaml.safe_dump(play_src, file, sort_keys=False)

# play = Play().load(play_src, variable_manager=variable_manager, loader=loader)
#
# #actually run it
# tqm = None
# try:
#     tqm = TaskQueueManager(
#             inventory=inventory,
#             variable_manager=variable_manager,
#             loader=loader,
#             options=options,
#             passwords=passwords,
#             stdout_callback="default",
#         )
#     result = tqm.run(play)
# finally:
#     if tqm is not None:
#         tqm.cleanup()
