function addContent() {
    event.preventDefault(); // Prevent default form submission

    // Disable the submit button
    $("#submit-button").prop("disabled", true);
    // Disable all radio buttons
    $('input[name="answer"]').prop("disabled", true);

    // Clear previous feedback
    $("#feedback").empty();

    let selectedOption = $('input[name="answer"]:checked').val(); // Get selected option

    let correctAnswer = $('#correct-answer').val();
    let questionId = question.id; // Access question ID directly from the question object


    // Compare selected option's ID with correct answer's ID
    if (selectedOption === correctAnswer) {
        $("#feedback").append('<p class="text-success">Correct!</p>');
    } else {
        // Display the correct image URL if the answer is incorrect
        $("#feedback").append('<p class="text-danger">Incorrect. The correct answer is: ' + correctAnswer + ')</p>');
    }

    // Log selected option
    console.log('Selected option:', selectedOption);

    // Send data to the server using AJAX
    $.ajax({
        type: "POST",
        url: "/submit-answer/" + questionId,
        data: {
            questionId: questionId,
            selectedOption: selectedOption,
            correctAnswer: correctAnswer
        },
        success: function(response) {
            console.log(response); // Log the response from the server
        },
        error: function(xhr, status, error) {
            console.error(error); // Log any errors
        }
    });
}

// Execute when the document is ready
$(document).ready(function () {
    $("#submit-button").click(addContent);
});
