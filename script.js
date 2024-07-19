// script.js
document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        displayResults(data.allocations);
        
        const downloadLink = document.getElementById('download-link');
        downloadLink.href = data.csv_download_url;
        downloadLink.style.display = 'block';
    } catch (error) {
        console.error('Error:', error);
    }
});

function displayResults(allocations) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    
    for (const allocation of allocations) {
        resultsDiv.innerHTML += `
            <p>Group ID: ${allocation.group_id}</p>
            <p>Hostel Name: ${allocation.hostel_name}</p>
            <p>Room Number: ${allocation.room_number}</p>
            <p>Members Allocated: ${allocation.members_allocated}</p>
            <hr>
        `;
    }
}