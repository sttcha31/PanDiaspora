"use client";

import Image from "next/image";
import { useRouter} from "next/navigation";

const Logo = () => {

    const router = useRouter();
    return (  
        <Image
            alt="Logo"
            className="hidden md:block"
            height={100}
            width={100}
            src="/images/mcgill-university-logo-png-transparent-cropped.png"
        />

    );
}
 
export default Logo;