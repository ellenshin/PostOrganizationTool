var likes = document.getElementById("likes")
var shares = document.getElementById("shares")
var comments = document.getElementById("comments")
var feeds = document.getElementById("feeds")

if (likes.textContent == " NA") {
    likes.style.color = "white"
}

if (shares.textContent == " NA") {
    shares.style.color = "white"
}

if (comments.textContent == " NA") {
    comments.style.color = "white"
}

var before_id_btn = document.getElementById("before_id")
var after_id_btn = document.getElementById("after_id")

if before_id_btn.getAttribute("href") == "//0" {
    before_id_btn.style.visibility = "hidden"
}

if after_id_btn.getAttribute("href") == "//0" {
    after_id_btn.style.visibility = "hidden"
}