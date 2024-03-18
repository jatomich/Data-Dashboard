import React from 'react';
import "@/app/globals.css";

export default function Page() {
    return (
        <div className="bg-white dark:bg-slate-800">
            <div className="shrink-0">
                <h1 className="text-3xl font-bold">Welcome to DATx</h1>
                <p className="text-lg">Your Data Exploration Playground.</p>
                <a href="/explore"><button type="submit"><h1>Start</h1></button></a>
            </div>
        </div>
    );
};

