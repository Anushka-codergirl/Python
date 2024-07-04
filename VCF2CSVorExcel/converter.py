import pandas as pd

def parse_vcf(file):
    contacts = []
    with open(file, 'r') as f:
        contact = {}
        for line in f:
            line = line.strip()
            if line.startswith('BEGIN:VCARD'):
                contact = {}
            elif line.startswith('END:VCARD'):
                contacts.append(contact)
            elif ':' in line:
                key, value = line.split(':', 1)
                contact[key] = value
    return contacts

vcf_file = 'contacts.vcf'
contacts = parse_vcf(vcf_file)
df = pd.DataFrame(contacts)
df.to_csv('contacts.csv', index=False)
df.to_excel('contacts.xlsx', index=False)