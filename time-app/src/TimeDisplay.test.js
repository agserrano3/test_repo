import React from 'react';
import { render, act } from '@testing-library/react';
import TimeDisplay from './TimeDisplay';

describe('TimeDisplay Component', () => {
  beforeAll(() => {
    jest.useFakeTimers(); // Use Fake timers to control time in test
  });

  afterAll(() => {
    jest.useRealTimers(); // cleanup to restore timers
  });

  it('should render', () => {
    const { asFragment } = render(<TimeDisplay />);
    expect(asFragment(<TimeDisplay />)).toMatchSnapshot();
  });

  it('should update time every second', () => {
    const { getByText, rerender }  = render(<TimeDisplay />);
    const timeElement = getByText(/AM|PM/i);
    const initialTime = timeElement.textContent;

    act(() => {
      jest.advanceTimersByTime(1000);
      rerender(<TimeDisplay />); // Rerender to update view with new time
    });

    expect(timeElement.textContent).not.toBe(initialTime);
  })
});