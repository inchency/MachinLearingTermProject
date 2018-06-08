import idaapi
import pickle

idaapi.autoWait()

save_path =idc.ARGV[1]

opcode = []

for seg_ea in Segments() :
    for func_ea in Functions(seg_ea, SegEnd(seg_ea)):
        f = idaapi.get_func(func_ea)
        func_opcode = []
        for block in idaapi.FlowChart(f):
            block_opcode = []
            for head in Heads(block.startEA, block.endEA):
                if isCode(GetFlags(head)) :
                    block_opcode.append('%02x' %(Byte(head)))
            func_opcode.append(block_opcode)
        opcode.append(func_opcode)

with open(save_path, 'wb') as f :
    pickle.dump(opcode, f)

idc.Exit(0)