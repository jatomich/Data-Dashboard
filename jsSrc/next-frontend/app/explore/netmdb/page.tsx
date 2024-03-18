import React from 'react';
import "@/app/globals.css";

// Fetch the records from the API
async function getRecords(){
const res = await fetch('http://127.0.0.1:8090/api/collections/NetflixIMDb/records');
const data = await res.json();

return data?.items as any[];
}

function Record({ record }: any) {
    const { id, tconst, title, director, cast, description } = record || {};

    return (
        <a href={`http://imdb.com/title/${tconst}`} target="_blank">
            <div>
                <h1>{title}</h1>
                <h2>{director}</h2>
                <h3>{cast}</h3>
                <p>{description}</p>
            </div>
        </a>
    );
}

// Add records to the NetflixIMDb table in PocketBase
// async function addRecords(){
// const records = await getRecords();
// const pocketBase = new PocketBase('NetflixIMDb');
// }

// Define the ExplorePage component
export default async function NetflixIMDbPage() {

    const records = await getRecords();

    return (
        <div className="max-w-2xl mx-auto antialiased pt-4 relative">

            <div className="h-[200vh] bg-black w-full dark:border dark:border-white/[0.1] rounded-md relative pt-40 overflow-clip">
                <h1>Netflix and IMDB Data</h1>
                <p>Netflix does not disclose ratings, but they are available on IMDb.
                    We{`&apos`}ve combined them here.
                </p>
                <div className="grid">
                    {records?.map((record) => {
                        return <Record key={record.id} record={record} />;
                        })}
                </div>
            </div>
        </div>
    );
};

