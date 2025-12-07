import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

interface ATSScoreProps {
    score: number;
}

export function ATSScore({ score }: ATSScoreProps) {
    const data = [
        { name: 'Score', value: score },
        { name: 'Remaining', value: 100 - score },
    ];

    const COLORS = ['#10b981', '#e5e7eb'];

    return (
        <div className="bg-white p-6 rounded-xl shadow-md border border-gray-100 flex flex-col items-center">
            <h3 className="text-lg font-semibold mb-4 text-gray-700">ATS Compatibility</h3>
            <div className="h-40 w-full relative">
                <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                        <Pie
                            data={data}
                            cx="50%"
                            cy="50%"
                            innerRadius={60}
                            outerRadius={80}
                            fill="#8884d8"
                            paddingAngle={5}
                            dataKey="value"
                            startAngle={90}
                            endAngle={-270}
                        >
                            {data.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                            ))}
                        </Pie>
                    </PieChart>
                </ResponsiveContainer>
                <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-3xl font-bold text-gray-800">{score}</span>
                </div>
            </div>
            <p className="text-sm text-gray-500 mt-2">Optimization Score</p>
        </div>
    );
}
