const video = document.getElementById('video')
var points = 0
var choice = ''

var imagesArray = ["/static/images/left.jpg", "/static/images/right.jpg", "/static/images/up.jpg", "/static/images/down.jpg"];
    function displayImage(){
      var num = Math.floor(Math.random() * 4);
      document.canvas.src = imagesArray[num];
        choice = imagesArray[num];}

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
    
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
     
    const landmarks = await faceapi.detectFaceLandmarks(video)
    const leftEye = landmarks.getNose();
    
    var initDic = leftEye[0];
    var getX = initDic["_x"];
    var getY = initDic["_y"];
    
       if (getX < 400){
        console.log("Right");
        
        if (choice == "/static/images/right.jpg"){
            throw new Error ("You lost!");
        }
        
        points = points + 1;

        } else if (getX > 400 && getX < 420){
            console.log("Mid");
        } else{
            console.log("Left");

            if (choice == "/static/images/left.jpg"){
                throw new Error ("You lost!");
            }

        } 
      
    
      
  }, 200)

        
})



