async function fetchFox() {
  const response = await fetch("https://randomfox.ca/floof/");
  const foxLink = await response.json();
  return foxLink["image"];
}

function changeFox() {
  foxPromise = Promise.resolve(fetchFox());
  foxPromise.then((imageLink) => {
    console.log(imageLink);
    document.getElementById("changeOnClick").src = imageLink;
  });
}

changeFox();
