import { style } from "@vanilla-extract/css";

export const quizContainer = style({
  height: "calc(100vh - 60px)",
  width: "100%",
  padding: "20px 0px 20px 65px ",
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
});
export const quizTitleContainer = style({
  position: "relative",
  height: "auto",
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
});
export const todayBg = style({
  width: "180px",
});
export const todayQuiz = style({
  fontSize: "2.3rem",
  position: "absolute",
  top: "40px",
  width: "250px",
  textAlign: "center",
  fontFamily: "Space Mono",
  color: "#202020",
  "@media": {
    "screen and (max-width: 768px)": {
      fontSize: "1.8rem",
    },
  },
});
export const questionNumbers = style({
  fontSize: "1.3rem",
  transform: "translateY(-20px)",
  textAlign: "center",
});
export const question = style({
  paddingBottom: "2rem",
  width: "100%",
  textAlign: "center",
  fontSize: "1.2rem",
});
export const quizAnswerDiv = style({
  display: "flex",
  flexDirection: "column",
  width: "100%",
  justifyContent: "center",
  alignItems: "center",
});

export const quizInput = style({
  // fontSize: "1rem",
  fontSize: "1.3rem",
  width: "60%",
  padding: "2rem 0rem",
  border: "0.5px solid #000000",
  borderRadius: "10px",
  marginBottom: "2rem",
  background: "white",
  textAlign: "center",
  overflow: "unset",
  resize: "none",
  height: "auto",

  ":focus": {
    outline: "none",
  },
});

export const questionInput = style([
  quizInput,
  {
    height: "auto",
    overflow: "unset",
  },
]);
export const quizButtonDiv = style({
  width: "80%",
  display: "flex",
  justifyContent: "space-evenly",
});
export const quizButton = style({
  backgroundColor: "#7982E8",
  border: "none",
  color: "white",
  width: "6rem",
  padding: "1rem",
  borderRadius: "15px",
  cursor: "pointer",
});
