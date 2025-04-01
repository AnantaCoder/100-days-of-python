
let dataTransfer = new DataTransfer();
let box = document.querySelectorAll("[role=textbox]")[1];
if (!box) {
  alert("No chat open, Make sure you have opened the chat you want to spam.");
  throw new Error(
    "No chat open, Make sure you have opened the chat you want to spam."
  );
}

// Get the number of messages to spam
var count = prompt(
  "Enter number of messages: \nPlease Enter a number between 0 and 100",
  "10"
);

if (!count || isNaN(count) || count < 0 || count > 1000) {
  alert(
    "Please enter only NUMBER between 0 and 100. \nYou can re-run the script now."
  );
} else {
  // Get the message to spam
  var message = prompt("MESSAGE YOU WANT TO SPAM : ", "Hello from spammer...");
  //make sure the user entered a message and it is not empty
  if (message == null || message == "") {
    alert("Please enter a message to spam. \nYou can re-run the script now.");
  } else {
    // Clear the current console for better visibility
    console.clear();
    dataTransfer.setData("text/plain", message);

    // spam the messages
    (async () => {
      for (let i = 0; i < count; i++) {
        // Get the input box

        box.focus();
        box.dispatchEvent(
          new ClipboardEvent("paste", {
            clipboardData: dataTransfer,

            // need these for the event to reach Draft paste handler
            bubbles: true,
            cancelable: true,
          })
        ); // trigger the event

        
        await new Promise((resolve) => setTimeout(resolve, 1000));
        // This is bit of stratch to select the send button and click it
        // You need to climb up the DOM tree three levels and then to second child and then the first child is the send button
        // ALternate option: (mainEl.querySelector('[data-testid="send"]') || mainEl.querySelector('[data-icon="send"]')).click();
        box.parentElement.parentElement.parentElement.children[1].children[0].click();
        console.log(`"${message}" sent -> ${i + 1} times`);
      }
    })();
  }
}