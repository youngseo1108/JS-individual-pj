let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget() {
  return Math.floor(Math.random() * 10);
}

function getAbsoluteDistance(guess, target) {
  if (guess < 0 | guess > 9) {
    alert('Wrong input. Should be between 0-9');
  } else {
    return Math.abs(guess - target);
  }
}

function compareGuesses(human, computer, target) {
  let human_guess = getAbsoluteDistance(human, target);
  let computer_guess = getAbsoluteDistance(computer, target);

  if (human_guess > computer_guess) {
    return false;
  }
  return true;
}

const updateScore = (winner) => {
  if (winner === 'human') {
    humanScore += 1;
  } else {
    computerScore += 1;
  }
}

const advanceRound = () => {
  currentRoundNumber += 1;
}