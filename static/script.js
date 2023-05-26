 function submitQuestion() {
        let question = document.getElementById("question").value;
        let answerPlaceholder = document.getElementById("answer-placeholder");
        let answerContent = document.getElementById("answer-content");

        // Show the answer placeholder
        answerPlaceholder.style.display = "block";
        answerContent.innerText = "Loading...";

        // Make the request to the server
        fetch("/answer", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "question=" + encodeURIComponent(question)
        })
            .then(response => response.text())
            .then(answer => {
                // Update the answer content
                answerContent.innerText = answer;
            })
            .catch(error => {
                // Handle any errors
                answerContent.innerText = "Error: " + error;
            });
    }