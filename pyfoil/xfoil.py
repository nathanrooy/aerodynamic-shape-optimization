#--- IMPORT DEPENDENCIES ------------------------------------------------------+

import os

#--- FUNCTIONS ----------------------------------------------------------------+

def run_xfoil():    

    # run xfoil
    os.system('xfoil < batch_bezier.txt')
    
    # read in results
    results_dict = read_xfoil_pacc_file('pacc_results.txt')
    
    # reset files
    os.system('rm -rf pacc_results.txt')
    
    return results_dict
    
    
def read_xfoil_pacc_file(file_name):
    with open(file_name) as f:
        for i, row in enumerate(f.readlines()):
            if i == 12:
                results = [item for item in row.replace('\n','').split(' ') if item != '']
    return {
        'alpha':float(results[0]),
        'cl':float(results[1]),
        'cd':float(results[2]),
        'cd_p':float(results[3]),
        'cm':float(results[4]),
        'top_xtr':float(results[5]),
        'bot_xtr':float(results[6])
        }
    

#--- EXAMPLE RUN --------------------------------------------------------------+

#print(run_xfoil())

#--- END ----------------------------------------------------------------------+
