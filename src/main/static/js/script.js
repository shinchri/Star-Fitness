console.log("Sanity Check")

// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler for monthly subscription
  let submitBtn = document.querySelector("#submitBtn1");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/1/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }

  // Event handler for yearly subscription
  let submitBtn2 = document.querySelector("#submitBtn2");
  if (submitBtn2 !== null) {
    submitBtn2.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/2/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});