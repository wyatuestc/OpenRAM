word_size = 2
num_words = 16

tech_name = "scn4m_subm"
process_corners = ["TT"]
supply_voltages = [ 5.0 ]
temperatures = [ 25 ]

output_path = "temp"
output_name = "sram_{0}_{1}_{2}".format(word_size,num_words,tech_name)

#Setting for multiport
netlist_only = True
bitcell = "pbitcell"
replica_bitcell="replica_pbitcell"
num_rw_ports = 1
num_r_ports = 1
num_w_ports = 1