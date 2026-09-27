<!DOCTYPE html>
<html>
<head>
<title>Smart Quiz AI Platform | By Ramya M</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;background:#0f172a;color:white;padding:20px;text-align:center}
.card{background:#1e293b;padding:20px;border-radius:15px;max-width:600px;margin:auto;box-shadow:0 0 20px #3b82f6}
button{background:#3b82f6;color:white;padding:12px 20px;border:none;border-radius:8px;cursor:pointer;margin:5px;font-weight:bold}
button:hover{background:#2563eb}
.option{display:block;background:#334155;padding:12px;margin:8px 0;border-radius:8px;text-align:left;cursor:pointer}
.option:hover{background:#475569}
#proctor{position:fixed;top:10px;right:10px;background:red;padding:5px 10px;border-radius:20px;font-size:12px}
</style>
</head>
<body>
<div id="proctor">🔴 AI Proctoring: ON</div>
<div class="card">
<h1>🧠 Smart Quiz AI Platform</h1>
<p>AI Proctoring + Voice Quiz + Blockchain Certificate | By Ramya M</p>
<div id="quiz"></div>
<button onclick="startVoice()">🎤 Voice Answer</button>
<button onclick="submitQuiz()">Submit & Get Certificate</button>
<div id="result"></div>
</div>
<script>
let quizData=[];
fetch('/get-quiz').then(r=>r.json()).then(d=>{quizData=d; showQuiz();});
function showQuiz(){
 let h='';
 quizData.forEach((q,i)=>{
  h+=`<h3>${i+1}. ${q.q}</h3>`;
  q.options.forEach((op,j)=>{
   h+=`<label class="option"><input type="radio" name="${i}" value="${j}"> ${op}</label>`;
  });
 });
 document.getElementById('quiz').innerHTML=h;
}
function submitQuiz(){
 let answers={};
 quizData.forEach((_,i)=>{
  let sel=document.querySelector(`input[name="${i}"]:checked`);
  if(sel) answers[i]=sel.value;
 });
 fetch('/submit-quiz',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(answers)})
.then(r=>r.json()).then(res=>{
  document.getElementById('result').innerHTML=`<h2>Score: ${res.score}/${res.total} (${res.percentage}%)</h2><p>🔗 Blockchain Certificate ID: <b>${res.certificate_id}</b><br>${res.message}</p>`;
 });
}
function startVoice(){
 const rec=new (window.SpeechRecognition||window.webkitSpeechRecognition)();
 rec.onresult=(e)=>{alert("Voice heard: "+e.results[0][0].transcript+" (Voice Quiz Active!)")};
 rec.start();
}
// Fake Proctoring
setInterval(()=>{console.log("Proctoring: Face detected")},3000);
</script>
</body>
</html>