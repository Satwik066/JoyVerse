import React from 'react';

const Letter = ({ letter, columnIndex, isSelected, onClick, reference }) => {
  return (
    <div
      className={`circle ${isSelected ? 'selected' : ''}`}
      onClick={() => onClick(columnIndex, letter)}
      ref={reference}
    >
      {letter}
    </div>
  );
};

export default Letter;
