vlan_normal=range(1, 1005)
vlan_extendida=range(1006, 4094)
numero_vlan=int(input("Ingrese un numero de vlan: "))

if numero_vlan in vlan_normal:
    print("El numero de la vlan", numero_vlan, "es del rango normal.")
elif numero_vlan in vlan_extendida:
    print("El numero de la vlan", numero_vlan, "es del rango extendida")
else:
    print("El numero de la vlan", numero_vlan, "no pertenece a ningun rango normal o extendida")