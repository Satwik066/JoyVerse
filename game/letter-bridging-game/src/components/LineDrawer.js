import React from 'react';

const LineDrawer = ({ positions, isValid }) => {
  if (positions.length < 2) return null;

  const lines = [];
  for (let i = 0; i < positions.length - 1; i++) {
    const { x: x1, y: y1 } = positions[i];
    const { x: x2, y: y2 } = positions[i + 1];

    lines.push(
      <line
        key={i}
        x1={x1}
        y1={y1}
        x2={x2}
        y2={y2}
        stroke="green"
        strokeWidth="3"
        strokeLinecap="round"
      />
    );
  }

  return (
    <svg className="line-drawer">
      {lines}
    </svg>
  );
};

export default LineDrawer;
