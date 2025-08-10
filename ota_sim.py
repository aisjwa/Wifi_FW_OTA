import argparse, time, random, semver, json, os
os.makedirs('reports', exist_ok=True)

def apply_update(target):
    # Fake states: download -> verify -> apply -> reboot -> health
    steps = ['download','verify','apply','reboot','health']
    log = []
    for s in steps:
        time.sleep(0.05)
        status = 'ok'
        if s=='health' and random.random()<0.05:
            status = 'fail'
        log.append({'step': s, 'status': status})
    return log

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', required=True, help='target version e.g. 2.3.1')
    args = ap.parse_args()
    assert semver.Version.parse(args.target)
    log = apply_update(args.target)
    open('reports/ota_log.json','w').write(json.dumps(log, indent=2))
    print('Saved reports/ota_log.json')
