const fs = require("fs");

fs.readFile("number_one.txt", "utf8", (err, data) => {
  if (err) {
    console.log("파일을 읽는 도중 오류가 발생했습니다.", err);
    return;
  }

  console.log("파일내용 :", data);
});

let content = "sysy";
fs.writeFile("number_four.txt", content, (err) => {
  if (err) {
    console.log("파일을 쓰는 도중 오류가 발생했습니다.", err);
    return;
  }
  console.log("파일 쓰기가 완료되었습니다.");
});

content = "hahahaha";
fs.appendFile("new_file.txt", content, (err) => {
  if (err) {
    console.log("파일을 쓰는 도중 오류가 발생했습니다.", err);
    return;
  }
  console.log("파일 쓰기가 완료되었습니다.");
});

content = "123123";
fs.appendFile("new_file.txt", content, (err) => {
  if (err) {
    console.log("파일을 쓰는 도중 오류가 발생했습니다.", err);
    return;
  }
  console.log("파일 쓰기가 완료되었습니다.");
});
