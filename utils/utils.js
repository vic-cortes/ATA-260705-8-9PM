// Comando para compiar el transcript
const CLASS = 'wyBDIb';

const transcript = [...document.querySelectorAll(`.${CLASS}`)]
  .map((el) => el.textContent.substring(0, 100))
  .join('\n');

console.log(transcript);
