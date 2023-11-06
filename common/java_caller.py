"""Modul that connects with the EXI jar files and does the encoding/decoding
"""
import os



def xml_to_binary(xml_file, output_file):
    
    
    
    
    cmd = 'java -jar common/encode.jar %s %s' % (xml_file, output_file)
    os.system(cmd)
    
'''
convert binary to xml 
'''
def binary_to_xml(binary_file, output_file):
    
    
    cmd = 'java -jar common/decode.jar %s %s' % (binary_file, output_file)
    os.system(cmd)



def main():
    
    print("Calling EXI java script")
    



if __name__ == "__main__":
    main()