#008. Ler o valor em metros e exiba convertido em centímetros e milímetros.

vm_d08 = float(input('Digite um valor em metros: '))
vc_d08 = float(vm_d08 * 100)
vmm_d08 = float(vm_d08 * 1000)
print('O valor digitado equivale a {} cm.'.format(vc_d08))
print('O valor digitado equivale a {} mm.'.format(vmm_d08))