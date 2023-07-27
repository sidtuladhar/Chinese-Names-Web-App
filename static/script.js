function searchNames() {
    const searchInput = document.getElementById('searchInput').value;
    fetch(`/search?q=${encodeURIComponent(searchInput)}`)
        .then(response => response.json())
        .then(data => displayResults(data));
}

function displayResults(results) {
    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = '';

    if (results.length === 0) {
        searchResults.innerHTML = '<p>No matches found.</p>';
    } else {
        const resultList = document.createElement('ul');
        results.forEach(result => {
            const listItem = document.createElement('li');
            listItem.textContent = `${result.Name} (Year: ${result.Year})`;
            resultList.appendChild(listItem);
        });
        searchResults.appendChild(resultList);
    }
}
