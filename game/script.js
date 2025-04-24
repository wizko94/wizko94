function startFishing(location) {
  let resultText = "";
  if (location === 'lake') {
    resultText = "Ти рибалиш на озері! Твоєму улову бути!";
  } else if (location === 'river') {
    resultText = "Ти рибалиш на річці! Підтягуй улов!";
  } else if (location === 'sea') {
    resultText = "Ти рибалиш на морі! Багато риб на горизонті!";
  }
  document.getElementById("result").innerText = resultText;
}
