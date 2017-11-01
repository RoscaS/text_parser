import os

PATH      = '{}\\FIXED'.format(os.getcwd())
START_TAG = '>>>>>HEAD'
END_TAG   = '====='

txt_files = [f for f in os.listdir() if f.endswith('.txt')]

lines   = []
fixed   = []
counter = 0
flag    = False

for file in txt_files:
    with open(file,'r') as original_file:

        lines = original_file.read().split('\n')

        for c, line in enumerate(lines):
            if START_TAG in line:
                counter += 1
                flag = True
            
            elif counter > 0:
                pass
            
            else:
                fixed.append(line)
            
            if END_TAG in line:
                counter -= 1
    
        if flag:
            if not os.path.exists(PATH):
                os.makedirs(PATH)

            with open(PATH+'\\fixed_'+file, 'a') as fixed_file:
                for line in fixed:
                    fixed_file.write(line+'\n')
            
            flag = False
            fixed.clear()

