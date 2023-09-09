function searchNames() {
    const searchInput = document.getElementById('name').value;
    console.log('Search Input:', searchInput);

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

function validateAndSearch() {
    const name = document.getElementById("name").value;
    const confirmName = document.getElementById("confirm_name").value;

    if (name !== confirmName) {
        alert("Names do not match. Please check and try again.");
    } else if (name === "" || confirmName === "") {
        alert("Please enter a name.");
    } else {
        // Names match, initiate the search
        searchNames();
    }
}
