import re
import sys

def convert_mysql_to_postgresql(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Common MySQL to PostgreSQL conversions
    replacements = [
        (r'ENGINE=InnoDB', ''),
        (r'ENGINE=MyISAM', ''),
        (r'AUTO_INCREMENT', 'SERIAL'),
        (r'INT\(\d+\)', 'INTEGER'),
        (r'TINYINT\(\d+\)', 'SMALLINT'),
        (r'TINYINT\(1\)', 'BOOLEAN'),
        (r'DATETIME', 'TIMESTAMP'),
        (r'UNSIGNED', ''),
        (r'COMMENT\s+\'.*?\',', ','),  # Remove comments
        (r'CHARACTER SET \w+', ''),
        (r'COLLATE \w+', ''),
        (r'`', '"'),  # Backticks to double quotes
        (r'\)\s*ENGINE.*?;', ');'),  # Remove engine declarations
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_mysql_to_pgsql.py input.sql output.sql")
        sys.exit(1)
    
    convert_mysql_to_postgresql(sys.argv[1], sys.argv[2])