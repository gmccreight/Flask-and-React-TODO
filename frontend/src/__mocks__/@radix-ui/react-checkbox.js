const React = require('react');

const Checkbox = {
  Root: ({ children, onCheckedChange, ...props }) => 
    React.createElement('div', { 
      role: 'checkbox', 
      onClick: () => onCheckedChange(true),
      ...props 
    }, children),
  Indicator: ({ children }) => 
    React.createElement('div', null, children),
};

module.exports = Checkbox;