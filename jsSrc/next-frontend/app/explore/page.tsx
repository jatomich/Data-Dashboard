import React from "react";
import "@/app/globals.css";

// Define the ExplorePage component
export default async function ExplorePage() {
    return (
        <>
        <div className="h-[800vh] bg-black w-full dark:border dark:border-white/[0.1] rounded-md relative pt-40 overflow-clip">
            <h1>Ready to Explore Some Data?</h1>
            <p>Make a Choice from the Selection Below</p>
            <div className="grid">
                <a href='explore/data'><button>NetflixIMDb</button></a>
                <a href='explore/gemini'><button>Google Gemini</button></a>
            </div>
        </div>
        </>
    );
};
