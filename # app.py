# app.py
from flask import Flask, request, jsonify, send_file
import csv
import io
from room_allocator import allocate_rooms

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']
    
    # Parse CSV files
    groups = parse_group_csv(group_file)
    hostels = parse_hostel_csv(hostel_file)
    
    # Allocate rooms
    allocations = allocate_rooms(groups, hostels)
    
    # Generate output CSV
    output = generate_output_csv(allocations)
    
    return jsonify({
        'allocations': allocations,
        'csv_download_url': '/download_csv'
    })

@app.route('/download_csv')
def download_csv():
    # Generate CSV file and send it as a downloadable file
    # Implementation details omitted for brevity
    pass

def parse_group_csv(file):
    # Parse the group CSV file
    # Implementation details omitted for brevity
    pass

def parse_hostel_csv(file):
    # Parse the hostel CSV file
    # Implementation details omitted for brevity
    pass

def generate_output_csv(allocations):
    # Generate the output CSV file
    # Implementation details omitted for brevity
    pass

if __name__ == '__main__':
    app.run(debug=True)