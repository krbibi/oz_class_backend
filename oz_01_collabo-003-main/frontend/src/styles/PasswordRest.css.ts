import { style } from "@vanilla-extract/css";

export const modalContainer = style({
  width: "100%",
  height: "100vh",
  position: "fixed",
  inset: 0,
  zIndex: 1000,
  backgroundColor: "rgba(0, 0, 0, 0.51)",
  backdropFilter: "blur(5px)",
});
export const passwordModal = style({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  width: "40%",
  height: "55%",
  backgroundColor: "white",
  position: "fixed",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -45%)",
  borderRadius: "20px",
  zIndex: 2,
  minWidth: "350px",
});
