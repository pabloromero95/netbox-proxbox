from proxmoxer import ProxmoxAPI
import pynetbox

from proxbox_api import NETBOX_SESSION as nb, NETBOX_CLUSTER_ID, NETBOX_ROLE_ID

# Cria VM/CT
def virtual_machine(proxmox_vm):
    # Salva VM/CT com informações básicas
    vm_json = {}
    vm_json["name"] = proxmox_vm['name']
    vm_json["status"] = 'active'
    vm_json["cluster"] = NETBOX_CLUSTER_ID      # Proxmox cluster
    vm_json["role"] = NETBOX_ROLE_ID        # Aplicacao
    
    # Cria VM/CT com json criado
    try:
        netbox_obj = nb.virtualization.virtual_machines.create(vm_json)

    except:
        print("[proxbox.create.virtual_machine] Falha na criação da VM")
        netbox_obj = None

    else:
        return netbox_obj

    # Caso nada funcione, volte erro
    netbox_obj = None
    return netbox_obj


