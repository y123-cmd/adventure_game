let currentStoryIndex = 0;
let story = [
    {
        text: "Welcome to the Adventure! Choose your path...",
        choices: [
            { text: "Enter the Dark Forest", action: 1 },
            { text: "Visit the Village", action: 2 }
        ]
    },
    {
        text: "You have entered the Dark Forest. The trees tower over you, and strange noises surround you.",
        choices: [
            { text: "Walk deeper into the forest", action: 3 },
            { text: "Turn back and leave", action: 4 }
        ]
    },
    {
        text: "You reach the Village. The villagers seem friendly, and there's a market nearby.",
        choices: [
            { text: "Talk to the villagers", action: 5 },
            { text: "Explore the market", action: 6 }
        ]
    },
    {
        text: "You walk deeper into the forest and encounter a wild beast! Fight or flee?",
        choices: [
            { text: "Fight the beast", action: 7 },
            { text: "Flee the forest", action: 8 }
        ]
    },
    {
        text: "You turn back and leave the forest, feeling safe. The adventure continues...",
        choices: [
            { text: "Continue your journey", action: 0 }
        ]
    },
    {
        text: "You talk to the villagers. They offer you help and supplies for your journey.",
        choices: [
            { text: "Accept their offer", action: 9 },
            { text: "Politely decline", action: 10 }
        ]
    },
    {
        text: "You explore the market. There are many items you could buy.",
        choices: [
            { text: "Buy a sword", action: 11 },
            { text: "Buy a potion", action: 12 }
        ]
    },
    {
        text: "You fight the beast and defeat it! Congratulations on your victory.",
        choices: [
            { text: "Continue your journey", action: 0 }
        ]
    },
    {
        text: "You flee the forest, but the wild beast follows you! Run faster!",
        choices: [
            { text: "Keep running", action: 13 },
            { text: "Turn and fight", action: 7 }
        ]
    },
    {
        text: "You accept the villagers' offer. They give you a map and a magical item!",
        choices: [
            { text: "Continue your journey", action: 0 }
        ]
    },
    {
        text: "You decline their offer. The villagers are sad, but you continue on your way.",
        choices: [
            { text: "Continue your journey", action: 0 }
        ]
    },
    {
        text: "You buy a sword! Now you're ready for battle.",
        choices: [
            { text: "Continue your journey", action: 0 }
        ]
    },
    {
        text: "You buy a potion! You're ready for whatever comes next.",
        choices: [
            { text: "Continue your journey", action: 0 }
        ]
    },
    {
        text: "You're running fast, but the beast catches up with you. It’s a tough fight!",
        choices: [
            { text: "Fight the beast", action: 7 },
            { text: "Keep running", action: 13 }
        ]
    }
];

function displayStory() {
    const storyText = document.getElementById('story-text');
    const choicesContainer = document.getElementById('choices-container');
    storyText.textContent = story[currentStoryIndex].text;
    choicesContainer.innerHTML = '';

    story[currentStoryIndex].choices.forEach(choice => {
        const button = document.createElement('button');
        button.classList.add('choice-btn');
        button.textContent = choice.text;
        button.onclick = () => {
            currentStoryIndex = choice.action;
            displayStory();
        };
        choicesContainer.appendChild(button);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    displayStory();
});
