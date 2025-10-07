import sys

ori_val = sys.argv[1]
esc_value = ori_val.replace(':', '\\:')
esc_value = esc_value.replace('/', '\\/')

sys.stdout.write(esc_value)
sys.stdout.flush()
sys.exit(0)
