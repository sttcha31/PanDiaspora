"use client";
import { useRouter } from 'next/navigation';
import Link from "next/link";
import {IconType} from "react-icons";
import { twMerge } from "tailwind-merge";

interface SidebarItemProps{
    label: string;
    active?: boolean;
    href: string;
}

const Usermenuitem: React.FC<SidebarItemProps> = ({
    label,
    active,
    href
}) => {
    const router = useRouter();
    return ( 
        <div
                    onClick={() => {   
                        if (active) {
                            router.push(href);
                        }       
                    }}         
                    className="
                        hidden 
                        md:block
                        text-sm
                        font-semiblock
                        py-3
                        px-4
                        rounded-full
                        hover:bg-neutral-100
                        transition
                        cursor-pointer
                    "
                >
                    {label}
        </div>
     );
}
 
export default Usermenuitem;