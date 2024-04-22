import json
from supabase import create_client

def retrieveAndConvertData():
    url = "https://ljzrkwoyewivcfhthral.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqenJrd295ZXdpdmNmaHRocmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA1NzU3NzcsImV4cCI6MjAxNjE1MTc3N30.bSMt5zZF012w-YVjnLTKJO0yAeMonr7VgserYfadoPM"
    supabase = create_client(url, key)
    
    # Retrieve the newest or bottom element from the table
    result = supabase.table('Raw').select('measurement').execute()
    result2 = supabase.table('Raw').select('id').execute()

    # Extract the measurement JSON
    measurement_json = result.data[-1]['measurement']
    id = result2.data[-1]['id']

    
    # Convert the measurement JSON into a 2D array
    measurement_array = json.loads(measurement_json)
    
    # Split the 2D array into separate lists for X, Y, and Z coordinates
    x_list = [reading['x'] for reading in measurement_array]
    y_list = [reading['y'] for reading in measurement_array]
    z_list = [reading['z'] for reading in measurement_array]


    return x_list, y_list, z_list, id

