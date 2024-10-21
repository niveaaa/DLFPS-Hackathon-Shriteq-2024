const images = [
    { src: 'images/1.jpg', label: 'ai' },
    { src: 'images/2.jpg', label: 'ai' },
    { src: 'images/3.jpg', label: 'ai' },
    { src: 'images/13.jpg', label: 'real' },
    { src: 'images/14.jpg', label: 'real' },
    { src: 'images/4.jpg', label: 'ai' },
    { src: 'images/5.jpg', label: 'ai' },
    { src: 'images/15.jpg', label: 'real' },
    { src: 'images/16.jpg', label: 'real' },
    { src: 'images/17.jpg', label: 'real' },
    { src: 'images/6.jpg', label: 'ai' },
    { src: 'images/7.jpg', label: 'ai' },
    { src: 'images/12.jpg', label: 'real' },
    { src: 'images/8.jpg', label: 'ai' },
    { src: 'images/18.jpg', label: 'real' },
    { src: 'images/19.jpg', label: 'real' },
    { src: 'images/9`.jpg', label: 'ai' },
    { src: 'images/20.jpg', label: 'real' },
    { src: 'images/21.jpg', label: 'real' },
    { src: 'images/10.jpg', label: 'ai' },
    { src: 'images/11.jpg', label: 'ai' },
    { src: 'images/22.jpg', label: 'real' }
    // Add more images as needed
];

let score = 0;
let currentImageIndex = 0;

function loadImage() {
    const quizImage = document.getElementById('quizImage');
    quizImage.src = images[currentImageIndex].src;
    document.getElementById('result').innerText = '';
    document.getElementById('nextBtn').style.display = 'none';
}

function updateScore() {
    document.getElementById('score').innerText = `Score: ${score}`;
}

document.querySelectorAll('.guessBtn').forEach(button => {
    button.addEventListener('click', function () {
        const guess = this.dataset.value;
        const correctAnswer = images[currentImageIndex].label;

        if (guess === correctAnswer) {
            score++;
            document.getElementById('result').innerText = 'Correct!';
        } else {
            document.getElementById('result').innerText = `Wrong! It was ${correctAnswer}.`;
        }

        updateScore();
        document.getElementById('nextBtn').style.display = 'block';
    });
});

document.getElementById('nextBtn').addEventListener('click', function () {
    currentImageIndex++;
    if (currentImageIndex < images.length) {
        loadImage();
    } else {
        document.getElementById('quizContainer').innerHTML = `
            <h2>Quiz Finished!</h2>
            <p>Your final score is: ${score} out of ${images.length}</p>
            <button id="restartBtn">Restart</button>
        `;
        document.getElementById('score').innerText = '';
        
        // Restart button functionality
        document.getElementById('restartBtn').addEventListener('click', () => {
            score = 0;
            currentImageIndex = 0;
            loadImage();
            updateScore();
            document.getElementById('quizContainer').innerHTML = `
                <img id="quizImage" src="" alt="Quiz Image" />
                <div id="options">
                    <button class="guessBtn" data-value="real">Real</button>
                    <button class="guessBtn" data-value="ai">AI Generated</button>
                </div>
                <div id="result"></div>
                <div id="score"></div>
                <button id="nextBtn" style="display: none;">Next</button>
            `;
        });
    }
});

// Load the first image when the page loads
loadImage();
updateScore();
