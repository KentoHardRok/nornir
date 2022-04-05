from nornir import init_nornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = init_nornir()

result = nr.run(
             napalm_get,
             getters=['get_facts'])

print_result(result)