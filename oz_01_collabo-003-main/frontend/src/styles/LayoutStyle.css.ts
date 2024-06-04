import { style } from "@vanilla-extract/css";

export const layout = style({
  display: "flex",
  width: "100%",
  position: "relative",
});
export const mainLayout = style({
  display: "flex",
  width: "100%",
  position: "relative",
  "@media": {
    "screen and (max-width: 900px)": {
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
    },
  },
});
export const logoLayout = style({
  width: "50%",
  display: "flex",
  position: "relative",
  height: "100vh",
  justifyContent: "center",
  alignItems: "center",
});
export const mainLogoLayout = style({
  width: "50%",
  display: "flex",
  position: "relative",
  height: "100vh",
  justifyContent: "center",
  alignItems: "center",
  "@media": {
    "screen and (max-width: 900px)": {
      height: 700,
    },
    "screen and (max-width: 500px)": {
      height: 600,
    },
  },
});
export const textLayout = style({
  width: "50%",
  display: "flex",
  position: "relative",
  height: "100vh",
  justifyContent: "center",
  alignItems: "center",
  "@media": {
    "screen and (max-width: 900px)": {
      display: "none",
    },
  },
});
export const iconBlue = style({
  position: "absolute",
  width: "23%",
  top: 0,
  right: 0,
  zIndex: 100,
});
export const logoPink = style({
  position: "absolute",
  height: "63%",
  bottom: "20",
  width: "auto",
  zIndex: 1,
});
export const logoYel = style({
  position: "absolute",
  height: "63%",
  width: "auto",
  // bottom: "20",
});

export const logoFont = style({
  fontFamily: "Swanky and Moo Moo",
  color: "#988888",
  zIndex: "999",
  fontSize: "18rem",
  letterSpacing: "10px",
  stroke: "#ffa5d8",
  strokeWidth: 3,
});
