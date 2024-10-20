document.getElementById('predictBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert("Please upload an image!");
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();
    
    reader.onload = async (event) => {
        const img = new Image();
        img.src = event.target.result;
        img.onload = async () => {
            // Use TensorFlow.js for predictions here
            const tensorImg = tf.browser.fromPixels(img).resizeNearestNeighbor([224, 224]).expandDims(0).toFloat().div(tf.scalar(255));
            
            // Load your model (make sure it's converted to TensorFlow.js format)
            const model = await tf.loadLayersModel('model/model.json');
            const prediction = model.predict(tensorImg).dataSync()[0];  // Get the prediction

            const label = prediction < 0.5 ? "AI Generated" : "Real";
            const confidence = Math.abs(prediction - 0.5) * 2;
            document.getElementById('result').innerHTML = `Prediction: ${label}, Confidence: ${confidence.toFixed(2)}`;
        }
    }
    
    reader.readAsDataURL(file);
});
