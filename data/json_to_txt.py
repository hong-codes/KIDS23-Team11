## convert json to txt
import json
import argparse

def json_to_text():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=str, default='open_assistant_5k_biomedical.json')
    parser.add_argument('--txt', type=str, default='open_assistant_5k_biomedical.txt')
    args = parser.parse_args()
    
    with open(args.json, 'r') as f:
        data = json.load(f)
	    
    with open(args.txt, 'w') as f:
        for i in range(len(data)):
            f.write('### dialogue: ' + str(i+1) + '\n\n')
            f.write(data[i]['labeled_dialog'])
            f.write('\n\n')
        f.close()
    
json_to_text()