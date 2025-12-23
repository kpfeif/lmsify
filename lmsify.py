import csv
import sys
import os

# Usage: python lmsify.py input.csv output.m3u

def ms_to_seconds(ms):
    try:
        return int(round(int(ms) / 1000))
    except Exception:
        return 0

def csv_to_m3u(input_csv, output_m3u):
    with open(input_csv, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_m3u, 'w', encoding='utf-8') as m3u:
            m3u.write('#EXTM3U\n')
            for row in reader:
                duration = ms_to_seconds(row.get('Duration (ms)', 0))
                artist = row.get('Artist Name(s)', '').strip()
                title = row.get('Track Name', '').strip()
                uri = row.get('Track URI', '').strip()
                # Write EXTINF line
                m3u.write(f'#EXTINF:{duration},{artist} - {title}\n')
                # Write URI (or path)
                m3u.write(f'{uri}\n')

def main():
    if len(sys.argv) != 3:
        print('Usage: python lmsify.py input.csv output.m3u')
        sys.exit(1)
    input_csv = sys.argv[1]
    output_m3u = sys.argv[2]
    if not os.path.exists(input_csv):
        print(f'Input file {input_csv} does not exist.')
        sys.exit(1)
    csv_to_m3u(input_csv, output_m3u)
    print(f'M3U playlist written to {output_m3u}')

if __name__ == '__main__':
    main()
